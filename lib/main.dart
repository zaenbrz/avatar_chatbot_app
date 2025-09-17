import 'package:flutter/material.dart';
import 'avatar_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false, // removes the debug banner
      title: '3D Avatar App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true, // optional, for Material 3 styling
      ),
      home: const AvatarScreen(), // 👈 sets AvatarScreen as the home page
    );
  }
}
