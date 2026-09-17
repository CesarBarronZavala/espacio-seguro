# 🌱 Espacio Seguro - Concienciación y Apoyo frente al Acoso

Plataforma web accesible, cálida y empática diseñada para que las personas puedan compartir testimonios sobre **acoso escolar (bullying)**, **laboral (mobbing)**, **cibernético** u otros tipos de acoso, acceder a líneas de apoyo psicológico 24/7 y encontrar contención en un entorno seguro y libre de juicios.

---

## 📋 Características Principales

- **Compartir relatos de forma segura**: Formulario con título, tipo de acoso, relato libre y fecha aproximada.
- **Anonimato total por defecto**: Opción de publicar de forma 100% anónima o con un alias/nombre visible si el usuario lo prefiere.
- **Moderación preventiva (Estado Pendiente)**: Todas las nuevas publicaciones pasan por revisión antes de hacerse públicas para evitar discursos de odio o datos personales de terceros.
- **Feed cronológico interactivo**: Muestra solo testimonios con estado publicado, más recientes primero, con filtros por categoría y buscador instantáneo.
- **Botón de empatía comunitaria**: Reacción *Te escuchamos* con contador de apoyo solidario.
- **Recursos de crisis 24/7 siempre visibles**: Barra superior permanente, botón flotante SOS y sección de contacto directo (911, Línea de la Vida, SAPTEL, Locatel CDMX).
- **Aviso de privacidad y protección de datos**: Información clara de que los datos no son comerciales y se puede solicitar el retiro de un testimonio en cualquier momento.
- **Panel de moderación integrado (dmin.html)**: Permite aprobar testimonios con 1 clic (publicado), rechazarlos o eliminarlos.
- **Base de datos Supabase (PostgreSQL)** con modo de respaldo local para pruebas inmediatas sin configuración previa.

---

## 🗄️ Estructura del Proyecto

`	ext
espacio-seguro-acoso/
├── index.html            # Página principal con feed, formulario y recursos
├── styles.css            # Estilos accesibles, paleta cálida y diseño responsive
├── app.js                # Lógica del cliente, validaciones y feed
├── admin.html            # Panel de moderación de testimonios
├── admin.js              # Lógica del panel de control y aprobación
├── supabase-config.js    # Configuración de credenciales de Supabase
├── schema.sql            # Script SQL de creación de tabla y políticas RLS
└── README.md             # Documentación y guía de despliegue
`

---

## 🚀 Guía de Configuración con Supabase (Paso a Paso)

### 1. Crear un proyecto en Supabase (Gratis)
1. Ve a [https://supabase.com](https://supabase.com) e inicia sesión o regístrate gratis.
2. Haz clic en **New Project**, elige un nombre (ej. espacio-seguro-db) y una contraseña para la base de datos.

### 2. Ejecutar el script schema.sql
1. En el menú lateral izquierdo de tu proyecto Supabase, entra a **SQL Editor**.
2. Haz clic en **New Query**.
3. Abre el archivo [schema.sql](schema.sql) de este proyecto, copia todo su contenido y pégalo en el editor.
4. Haz clic en **Run** (o presiona Ctrl + Enter).
5. ¡Listo! Se creará la tabla experiencias con sus políticas de seguridad (RLS) y testimonios iniciales.

### 3. Conectar la aplicación
1. En Supabase, ve a **Project Settings** (el icono de engranaje ⚙️) > **API**.
2. Copia:
   - **Project URL** (ejemplo: https://abcdefgh.supabase.co)
   - **anon / public key** (clave pública que empieza por eyJ...)
3. Puedes pegarlas de dos formas:
   - **Opción A (Recomendada):** Abre la página web, haz clic en el botón superior **⚙️ Base de datos**, pega los valores y haz clic en *Guardar y Conectar*.
   - **Opción B:** Edita el archivo supabase-config.js y asigna tus variables directamente.

---

## 🛡️ Panel de Moderación (dmin.html)

Para revisar testimonios en estado pendiente:
1. Abre dmin.html en tu navegador o haz clic en el botón **🛡️ Moderar** en la cabecera.
2. Ingresa la clave de moderación:
   - **Clave por defecto:** moderador2026
3. Verás tres pestañas:
   - ⏳ **Pendientes**: Nuevos testimonios enviados por usuarios. Haz clic en **✅ Aprobar y Publicar en el Feed** para que aparezca en la página principal, o **🚫 Rechazar**.
   - ✅ **Publicados**: Testimonios activos en el feed público.
   - 🗑️ **Rechazados**: Testimonios descartados.

---

## 🌐 Cómo Alojar la Web Gratis

Al ser una aplicación web estática (HTML, CSS, JS), puedes publicarla en minutos en cualquiera de estas opciones:

### Opción 1: Netlify
1. Ve a [https://app.netlify.com/drop](https://app.netlify.com/drop).
2. Arrastra la carpeta del proyecto (espacio-seguro-acoso).
3. En segundos tendrás una URL pública HTTPS gratuita lista para compartir.

### Opción 2: Vercel
1. Instala el CLI de Vercel con 
pm i -g vercel y corre ercel dentro de la carpeta, o conecta el repositorio en [vercel.com](https://vercel.com).

### Opción 3: GitHub Pages
1. Sube los archivos a un repositorio en GitHub.
2. Ve a **Settings** > **Pages** y selecciona la rama main (directorio /root).

---

## 🔒 Privacidad y Ética

- **Sin Rastreo:** No se almacenan cookies de seguimiento comercial ni se solicitan datos personales reales obligatorios.
- **Protección de Datos:** Las personas pueden solicitar la eliminación de cualquier relato en cualquier momento escribiendo al correo configurado en el aviso de privacidad.
- **Contención Profesional:** Este sitio no reemplaza la atención psicológica ni médica profesional.

---
*Hecho con empatía para construir comunidades más seguras y solidarias.*
