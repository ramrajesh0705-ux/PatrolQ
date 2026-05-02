def select_features(df):
    return df[[
        "Latitude", "Longitude",
        "hour", "month","day_num",
        "Arrest", "Domestic"
    ]]
