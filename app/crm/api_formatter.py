def create_json_response(client, client_wallet, created, sample_success_response):

    new_response = sample_success_response

    new_response['data']['client_info']['cid'] = client.cid
    new_response['data']['client_info']['first_name'] = client.first_name
    new_response['data']['client_info']['last_name'] = client.last_name
    new_response['data']['client_info']['country_code'] = client.country_code
    new_response['data']['client_info']['email'] = client.email
    new_response['data']['client_info']['address'] = client.address
    new_response['data']['client_info']['phone'] = client.phone
    new_response['data']['client_info']['created_at'] = client.created
    new_response['data']['client_info']['last_modified'] = client.updated
    
    if not created:
        new_response['data']['client_finance']['total_balance'] = client_wallet.total_balance
        new_response['data']['client_finance']['available_balance'] = client_wallet.available_balance
        new_response['data']['client_finance']['lien_balance'] = client_wallet.lien_balance
        new_response['data']['client_finance']['created_at'] = client_wallet.created
        new_response['data']['client_finance']['last_modified'] = client_wallet.updated

    else:
        for key, value in new_response['data']['client_finance'].items():
            new_response['data']['client_finance'][key] = 0.00
    return new_response