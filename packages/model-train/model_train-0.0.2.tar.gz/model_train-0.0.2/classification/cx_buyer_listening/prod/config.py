dict_source = {
    "app_review": {
        "string_cols": ["Subject", "Body", "raw_text"],
        "select_cols": ["Date", "create_date"],
    },
    "kompa": {
        "string_cols": ["Title", "Content"],
        "select_cols": [
            "Id",
            "Topic",
            "UrlComment",
            "UrlTopic",
            "SiteName",
            "AuthorId",
            "PublishedDate",
        ],
    },
    "nps": {
        "string_cols": ["user_fill_text"],
        "select_cols": ["date_submitted", "userid"],
        "api_endpoint": "https://datasuite.shopee.io/datahub/api/v1/usertoken/upload/csv/csv-8818b2cb-98f6-427c-8ada-42620b44a11b",
        "ingestion_token": "507878de-8603-448f-b2bc-d1113b158655"
    }
}