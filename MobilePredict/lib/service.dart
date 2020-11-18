import 'dart:convert';

import 'package:http/http.dart';

class Services{

  static void Predict(body)async{
    
    String url = 'http://192.168.1.11/predict';
    Map<String,String> headers = {"Content-Type":"application/json"}; 

    String requestBody = jsonEncode({body});

    Response response = await post(url,
                                    headers: headers,
                                    body: requestBody);
    
    String responseBody = response.body;
    print(responseBody);
  }
}