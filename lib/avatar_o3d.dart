import 'package:flutter/material.dart';
import 'package:o3d/o3d.dart';

class AvatarScreen extends StatefulWidget {
  const AvatarScreen({super.key});

  @override
  State<AvatarScreen> createState() => _AvatarScreenState();
}

class _AvatarScreenState extends State<AvatarScreen> {
  final O3DController controller = O3DController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("My Avatar")),
      body: O3D(
        src: 'assets/models/68c2c316912b35fdec9c8a53.glb',
        controller: controller,
        autoRotate: true,
        autoPlay: true,
        cameraControls: true,
      ),
    );
  }
}
