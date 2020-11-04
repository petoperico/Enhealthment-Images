import 'package:flutter/material.dart';
import 'package:Enhealthment_app/UploadImage.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Enhealtment Images',
      debugShowCheckedModeBanner: false,
      home: UploadImage(),
    );
  }
}
