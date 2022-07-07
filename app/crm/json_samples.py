sample_success_response = {
    "message":"successful",
    "data" :{
        "client_info": { 
            "created_at":"2022-07-04T05:57:38.954Z",
            "last_modified": "2024-07-04T05:57:38.954Z",
            "first_name":"Pansy",
            "last_name":"Koepp",
            "email":"Keshaun.Turner@yahoo.com",
            "address":"7533 Hettinger Junction",
            "phone":"980-969-1470",
            "country_code":"SA",
            "cid":65437
        },
        
        "client_finance" : {
            "total_balance" : 122.55,
            "available_balance" : 340.85,
            "lien_balance" : 73.20,
        }
    }
}


sample_error_response = {
    "status": "false",
    "message": "error, invalid cid"
}