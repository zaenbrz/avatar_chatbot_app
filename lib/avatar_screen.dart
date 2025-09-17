import 'package:flutter/material.dart';
import 'package:model_viewer_plus/model_viewer_plus.dart';

class AvatarScreen extends StatelessWidget {
  const AvatarScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("My Avatar")),
      body: Center(
        child: ModelViewer(
          src: 'assets/models/avatar.glb',
          alt: "A 3D avatar",
          autoRotate: true,
          cameraControls: true,
          backgroundColor: Colors.white,
          animationName: 'hello',
          autoPlay: true,
        ),
      ),
    );
  }
}
