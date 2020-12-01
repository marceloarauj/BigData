import 'dart:convert';

import 'package:MobilePredict/models/classe_model.dart';
import 'package:http/http.dart';

class Services {
  static Future<ClasseModel> predict(body) async {
    ClasseModel classe;
    String url = 'https://bigdatapredict.herokuapp.com/predict';
    Map<String, String> headers = {"Content-Type": "application/json"};

    String requestBody = jsonEncode(body);

    Response response = await post(url, headers: headers, body: requestBody);

    String responseBody = response.body;
    if (requestBody != null) {
      classe = ClasseModel.fromJson(json.decode(responseBody));
    }
    return classe;
  }
}
