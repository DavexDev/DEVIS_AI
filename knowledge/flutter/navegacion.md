# Flutter — Navegación y Rutas

## Ejecutar en Web

```bash
flutter run -d chrome
```

> En Flutter Web, `go_router` es la opción **recomendada** porque sincroniza las rutas con la URL del navegador (`/detalle/42` aparece en la barra de direcciones). `Navigator.push` también funciona pero no actualiza la URL.

## Navigator básico (push / pop)

```dart
// Navegar a una nueva pantalla
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => const DetalleScreen()),
);

// Volver a la pantalla anterior
Navigator.pop(context);

// Enviar datos al volver
Navigator.pop(context, 'resultado');

// Reemplazar pantalla actual (sin poder volver)
Navigator.pushReplacement(
  context,
  MaterialPageRoute(builder: (context) => const HomeScreen()),
);
```

## Rutas nombradas

```dart
// main.dart — definir rutas
MaterialApp(
  initialRoute: '/',
  routes: {
    '/':       (context) => const HomeScreen(),
    '/detalle': (context) => const DetalleScreen(),
    '/perfil':  (context) => const PerfilScreen(),
  },
);

// Navegar por nombre
Navigator.pushNamed(context, '/detalle');

// Pasar argumentos con rutas nombradas
Navigator.pushNamed(
  context,
  '/detalle',
  arguments: {'id': 42, 'titulo': 'Flutter'},
);

// Recibir argumentos en la pantalla destino
class DetalleScreen extends StatelessWidget {
  const DetalleScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final args = ModalRoute.of(context)!.settings.arguments
        as Map<String, dynamic>;
    return Scaffold(
      appBar: AppBar(title: Text(args['titulo'])),
      body: Center(child: Text('ID: ${args['id']}')),
    );
  }
}
```

## go_router (navegación declarativa moderna)

```yaml
# pubspec.yaml
dependencies:
  go_router: ^13.0.0
```

```dart
import 'package:go_router/go_router.dart';

// Definir el router
final GoRouter _router = GoRouter(
  routes: [
    GoRoute(
      path: '/',
      builder: (context, state) => const HomeScreen(),
    ),
    GoRoute(
      path: '/detalle/:id',
      builder: (context, state) {
        final id = state.pathParameters['id']!;
        return DetalleScreen(id: id);
      },
    ),
    GoRoute(
      path: '/perfil',
      builder: (context, state) => const PerfilScreen(),
    ),
  ],
);

// Usar en MaterialApp
MaterialApp.router(
  routerConfig: _router,
);

// Navegar
context.go('/detalle/42');         // reemplaza
context.push('/perfil');           // apila
context.pop();                     // vuelve atrás
```

## BottomNavigationBar con navegación por índice

```dart
class MainScreen extends StatefulWidget {
  const MainScreen({super.key});
  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int _currentIndex = 0;

  final List<Widget> _screens = const [
    HomeScreen(),
    BuscarScreen(),
    PerfilScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) => setState(() => _currentIndex = index),
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home),   label: 'Inicio'),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: 'Buscar'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Perfil'),
        ],
      ),
    );
  }
}
```

## WillPopScope — Confirmar salida

```dart
WillPopScope(
  onWillPop: () async {
    final salir = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('¿Salir?'),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('No')),
          TextButton(onPressed: () => Navigator.pop(ctx, true),  child: const Text('Sí')),
        ],
      ),
    );
    return salir ?? false;
  },
  child: Scaffold(...),
);
```
