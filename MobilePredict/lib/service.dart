import 'dart:convert';

import 'package:http/http.dart';

class Services{

  static Future<String> Predict(body)async{
    
    String url = 'http://181.223.204.40:5000/predict';
    Map<String,String> headers = {"Content-Type":"application/json"}; 

    String requestBody = jsonEncode(body);

    Response response = await post(url,
                                    headers: headers,
                                    body: requestBody);
    
    String responseBody = response.body;

    return responseBody;
  }
}