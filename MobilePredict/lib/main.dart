import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mobile Predict',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.amber,
      ),
      home: MyHomePage(title: 'Predição de dados'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool deveExibirMetricas = false;
  bool deveExibirFoto = false;
  int model = 0;
  int metric = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text(widget.title),
        ),
        body: Center(
            child: Column(children: <Widget>[
          Padding(
            padding: EdgeInsets.only(top: 30),
            child: Container(
                width: MediaQuery.of(context).size.width * 0.8,
                height: 60,
                child: DropdownButton(
                  isExpanded: true,
                  items: _models(),
                  value: model,
                  icon: Icon(Icons.desktop_windows),
                  onChanged: (valor) {
                    setState(() {
                      model = valor;
                    });
                  },
                )),
          ),
          Padding(
            padding: EdgeInsets.only(top: 30),
            child: Container(
                width: MediaQuery.of(context).size.width * 0.8,
                height: 60,
                child: DropdownButton(
                  isExpanded: true,
                  items: _metrics(),
                  value: metric,
                  icon: Icon(Icons.data_usage),
                  onChanged: (valor) {
                    setState(() {
                      model = valor;
                    });
                  },
                )),
          )
        ])));
  }

  List<DropdownMenuItem> _models() {
    return [
      DropdownMenuItem(
        child: Text('Nearest Neighbors'),
        value: 0,
      ),
      DropdownMenuItem(
        child: Text('Random Forest'),
        value: 1,
      ),
      DropdownMenuItem(
        child: Text('Decision Tree'),
        value: 2,
      ),
      DropdownMenuItem(
        child: Text('Naive Bayes'),
        value: 3,
      )
    ];
  }

  List<DropdownMenuItem> _metrics() {
    return [
      DropdownMenuItem(
        child: Text('Accuracy'),
        value: 0,
      ),
      DropdownMenuItem(
        child: Text('f1'),
        value: 1,
      ),
      DropdownMenuItem(
        child: Text('Precision'),
        value: 2,
      ),
      DropdownMenuItem(
        child: Text('Recall'),
        value: 3,
      )
    ];
  }
}
