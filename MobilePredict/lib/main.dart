import 'package:camera/camera.dart';
import 'package:flutter/material.dart';

Future<void> main() async {

  WidgetsFlutterBinding.ensureInitialized();
  final cameras = await availableCameras();
  final firstCamera = cameras.first;

  runApp(
    MaterialApp(
      theme: ThemeData.dark(),
      debugShowCheckedModeBanner: false,
      home: MyApp(
        camera: firstCamera,
      ),
    ),
  );
}

class MyApp extends StatelessWidget {
  CameraDescription camera;

  MyApp({this.camera});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mobile Predict',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.amber,
      ),
      home: MyHomePage(title: 'Predição de dados',camera: camera,),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title, this.camera}) : super(key: key);

  final String title;
  final CameraDescription camera;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool deveExibirMetricas = false;
  bool deveExibirFoto = false;
  int model = 0;
  int metric = 0;
  CameraController _controller;
  Future<void> _initializeControllerFuture;

  @override
  void initState() {
    super.initState();
    _controller = CameraController(
      widget.camera,
      ResolutionPreset.medium,
    );

    _initializeControllerFuture = _controller.initialize();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

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
          ),
          Padding(
            padding: EdgeInsets.only(top: 30),
            child: Container(
              width: MediaQuery.of(context).size.width * 0.8,
              height: 300,
              child: FutureBuilder<void>(
                future: _initializeControllerFuture,
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.done) {
                    return CameraPreview(_controller);
                  } else {
                    return Center(child: CircularProgressIndicator());
                  }
                },
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(top:30),
            child: Container(

              width: MediaQuery.of(context).size.width * 0.8,
              height: 40,
              child: RaisedButton(
                  child: Text('Enviar'), 
                  onPressed: ()=>{
                    
                  },                          
              ),
              
            ),
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
