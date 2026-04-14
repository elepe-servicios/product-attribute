# Validación de Migración - product_template_tags

## Tests manuales post-migración

### 1. Instalación del módulo
```bash
# Opción 1: Línea de comandos
odoo-bin -d <database> -u product_template_tags

# Opción 2: Interfaz web
Apps → Buscar "Product Template Tags" → Actualizar/Instalar
```

### 2. Tests funcionales básicos

#### 2.1 Crear un tag simple
1. Ir a: Inventario → Configuración → Product Tags
2. Crear un nuevo tag:
   - Nombre: "Test Tag V19"
   - Color: Seleccionar un color
   - Guardar

**Resultado esperado:** ✅ Tag creado sin errores

#### 2.2 Crear tag jerárquico
1. Crear tag padre: "Electrónica"
2. Crear tag hijo:
   - Nombre: "Computadoras"
   - Parent Tag: "Electrónica"
   - Guardar

**Resultado esperado:** ✅ Jerarquía visible como "Electrónica / Computadoras"

#### 2.3 Asignar tag a producto
1. Ir a: Inventario → Productos → Productos
2. Seleccionar/crear un producto
3. En la pestaña General, campo "Tags":
   - Agregar el tag "Test Tag V19"
   - Guardar

**Resultado esperado:** ✅ Tag visible en el producto

#### 2.4 Verificar vista Kanban
1. Ir a: Inventario → Productos → Productos
2. Cambiar a vista Kanban
3. Verificar que los tags se muestran con colores

**Resultado esperado:** ✅ Tags visibles en tarjetas kanban

#### 2.5 Filtrar por tags
1. En la lista de productos
2. Usar el filtro de búsqueda
3. Buscar por el tag creado

**Resultado esperado:** ✅ Productos filtrados correctamente

#### 2.6 Contador de productos
1. Ir al tag creado
2. Verificar el botón con contador de productos
3. Hacer clic en el botón

**Resultado esperado:** ✅ Muestra productos asociados

#### 2.7 Test multi-compañía (si aplica)
1. Crear/seleccionar otra compañía
2. Crear tag con mismo nombre pero otra compañía
3. Guardar

**Resultado esperado:** ✅ Sin error de duplicado (diferentes compañías)

4. Intentar crear tag con mismo nombre y misma compañía
**Resultado esperado:** ❌ Error de unicidad (correcto)

#### 2.8 Test de recursión
1. Crear tag: "A"
2. Crear tag: "B" con parent "A"
3. Intentar editar tag "A" y poner parent "B"

**Resultado esperado:** ❌ Error de recursión (correcto)

### 3. Tests automatizados

```bash
# Ejecutar tests del módulo
odoo-bin -d <database> -i product_template_tags --test-enable --stop-after-init --log-level=test

# Buscar en el log:
# - "test_product_template_tag" → PASSED
# - "test_product_template_tag_uniq" → PASSED
```

### 4. Verificación de logs

Revisar el archivo de log de Odoo para asegurar que no hay:
- ❌ Errores (ERROR)
- ❌ Warnings críticos
- ✅ Solo mensajes informativos

### 5. Verificación de rendimiento

1. Crear 100+ tags
2. Asignar múltiples tags a productos
3. Verificar tiempo de respuesta en:
   - Lista de productos
   - Vista kanban
   - Filtros de búsqueda

**Resultado esperado:** ✅ Tiempo de respuesta aceptable (< 2 segundos)

---

## Checklist de validación completa

- [ ] Módulo instalado sin errores
- [ ] Crear tags simples funciona
- [ ] Crear tags jerárquicos funciona
- [ ] Asignar tags a productos funciona
- [ ] Vista Kanban muestra tags correctamente
- [ ] Filtros por tags funcionan
- [ ] Contador de productos es correcto
- [ ] Multi-compañía funciona (si aplica)
- [ ] Restricción de recursión funciona
- [ ] Restricción de unicidad funciona
- [ ] Tests automatizados pasan
- [ ] No hay errores en logs
- [ ] Rendimiento es aceptable
- [ ] Migración de datos existentes funciona (si aplica)

---

## Problemas comunes y soluciones

### Problema 1: Error al instalar el módulo
**Solución:** 
- Verificar que la versión de Odoo sea 19.0
- Limpiar caché del navegador
- Reiniciar el servidor Odoo

### Problema 2: Tags no aparecen en vista Kanban
**Solución:**
- Limpiar assets: `odoo-bin -d <database> --update=product_template_tags`
- Refrescar el navegador con Ctrl+F5

### Problema 3: Error de permisos
**Solución:**
- Verificar que el usuario tenga permisos adecuados
- Revisar archivos en `security/`

### Problema 4: Tests fallan
**Solución:**
- Verificar que la base de datos esté actualizada
- Ejecutar: `odoo-bin -d <database> -u base,product,product_template_tags`

---

## Contacto y soporte

Si encuentra algún problema durante la validación:
1. Revisar archivo `MIGRATION.md` para detalles técnicos
2. Verificar logs de Odoo
3. Consultar documentación de OCA
4. Reportar issue en repositorio OCA

---

**Documento de validación**  
Versión: 1.0  
Fecha: 4 de marzo de 2026
