import 'dart:convert';

import 'package:http/http.dart';

class Services{

  static Future<String> Predict(body)async{
    
    String url = 'https://bigdatapredict.herokuapp.com/predict';
    Map<String,String> headers = {"Content-Type":"application/json"}; 

    String requestBody = jsonEncode(body);

    Response response = await post(url,
                                    headers: headers,
                                    body: requestBody);
    
    String responseBody = response.body;
    Map classe = json.decode(responseBody);
    
    return classe['class'];
  }
}