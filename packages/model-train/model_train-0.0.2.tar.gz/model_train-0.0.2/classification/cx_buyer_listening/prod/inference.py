from pathlib import Path
import polars as pl
from rich import print
from core_pro.ultilities import make_dir, make_sync_folder
from core_eda import TextEDA
from core_pro import AWS
from datasets import Dataset
from tqdm.auto import tqdm
import re
from collections import defaultdict
import sys

sys.path.extend([str(Path.home() / "PycharmProjects/model_train")])
from src.model_train.pipeline_infer import InferenceTextClassification
from config import dict_source


# path
path = make_sync_folder("cx/buyer_listening/inference/2025")
files = sorted([*path.glob("app_review/*.xlsx")])

# model
path_model = "kevinkhang2909/buyer_listening"
infer = InferenceTextClassification(
    pretrain_name=path_model,
    torch_compile=False,
    fp16=True,
    task_type="multi_classes",
)

def run(file_path: Path):
    # init source:
    folder = file_path.parts[-2]
    print(f"=== START {file_path.name} ===")

    # create path
    path_export = path / folder / "result"
    make_dir(path_export)
    file_name = file_path.stem
    file_name = '_'.join(re.sub(r"\.", "", file_name.lower()).split(' '))
    file_export = path_export / f"{file_name}.parquet"
    if file_export.exists():
        print(f"Batch Done: {file_export.stem}")
        return None, None, file_export

    # data
    if folder == "nps":
        df = pl.read_parquet(file_path)
    else:
        df = pl.read_excel(file_path, engine="openpyxl")
    string_cols = [i for i in dict_source[folder]["string_cols"] if i in df.columns]
    select_cols = [i for i in dict_source[folder]["select_cols"] if i in df.columns]

    # clean data
    lst = {
        col: [TextEDA.clean_text_multi_method(_) for _ in df[col]]
        for col in tqdm(string_cols, desc="[TextEDA] Clean Text")
    }
    if not select_cols:
        df_clean = pl.DataFrame(lst)
    else:
        df_clean = pl.concat([df[select_cols], pl.DataFrame(lst)], how="horizontal")
    df_clean = (
        df_clean
        .with_columns(
            pl.concat_str([pl.col(i) for i in string_cols], separator=". ").alias("text")
        )
    )

    # infer
    ds_pred = infer.run_pipeline(Dataset.from_polars(df_clean), text_column="text")

    # post process
    ds_pred_post = (
        ds_pred.to_polars()
        .with_columns(
            pl.col("labels").str.split(" >> ").list[i].alias(v)
            for i, v in enumerate(["l1_pred", "l2_pred"])
        )
        .drop(["labels"])
        .with_columns(pl.lit(f"{f.stem}").alias("file_source"))
    )

    if folder == "kompa":
        ds_pred_post = ds_pred_post.with_columns(
            pl.col("PublishedDate").alias("grass_date"),
            pl.col('AuthorId').cast(pl.String),
            pl.col("score").cast(pl.Float32),
        )
    elif folder == "app_review":
        ds_pred_post = (
            ds_pred_post
            .rename({"date": "create_date"})
            .with_columns(pl.col("score").cast(pl.Float32))
            .select(["create_date", "text", "score", "l1_pred", "l2_pred", "file_source"])
        )
        if ds_pred_post["create_date"].dtype == pl.String:
            lst = [
                pl.col("create_date").str.to_date(),
                pl.col("create_date").str.to_date().alias("grass_date"),
            ]
        else:
            lst = [pl.col("create_date").alias("grass_date")]
        ds_pred_post = ds_pred_post.with_columns(lst)

    elif folder == "nps":
        ds_pred_post = (
            ds_pred_post.with_columns(
                pl.col("date_submitted").str.to_date("%Y-%m-%d", strict=False),
                pl.col("date_submitted").str.to_date("%Y-%m-%d", strict=False).alias("grass_date"),
                pl.col("score").cast(pl.Float32),
            )
            .filter(pl.col("text") != "")
        )

    # export
    ds_pred_post.columns = [i.lower() for i in ds_pred_post.columns]
    ds_pred_post.write_parquet(file_export)
    return df, ds_pred_post, file_export


lst = defaultdict(list)
for f in files:
    # df = pl.read_excel(files[6], engine="openpyxl")
    df, df_tag, file_export = run(f)
    folder = file_export.parts[-3]
    lst[folder].append(file_export)
    # break

# file = path / "nps/free_text.parquet"
# df, df_tag, file_export = run(file)

bucket_name = 'sg-vnbi-ops-kevin'
s3 = AWS(bucket_name)
prefix = "cx/buyer_listening/kompa"
# files = s3.get_all_files(prefix)
# s3.delete_file(files)
# s3.upload_multiple_files(lst['kompa'], prefix)

prefix = "cx/buyer_listening/app_review"
# s3.get_all_files(prefix)
# s3.upload_multiple_files(lst['app_review'], prefix)
