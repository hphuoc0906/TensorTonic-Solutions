def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """

    user_info = []
    for user in requests:
        user_id = user['user_id']
        get_info = user['online_features']
        if user_id in feature_store:
            get_info.update(feature_store[user_id])
        else:
            get_info.update(defaults)
        user_info.append(get_info)

    return user_info