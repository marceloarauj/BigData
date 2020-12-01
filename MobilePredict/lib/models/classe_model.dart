class ClasseModel {
  String nome;

  ClasseModel({this.nome});

  static ClasseModel fromJson(Map<String, dynamic> json) {
    ClasseModel model = ClasseModel();
    if (json['class'] != null) {
      model.nome = json['class'];
    }
    return model;
  }
}
