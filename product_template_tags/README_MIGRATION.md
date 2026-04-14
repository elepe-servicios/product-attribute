# 📦 product_template_tags - Migración V19

## ℹ️ Información del módulo

**Versión:** 19.0.1.0.0  
**Autor:** ACSONE SA/NV, Numigi, OCA  
**Licencia:** AGPL-3  
**Estado:** ✅ Migrado y validado para Odoo 19.0

---

## 📄 Documentación de migración

Este módulo ha sido migrado de Odoo V17 a V19 siguiendo los lineamientos oficiales de OCA.

### Documentos disponibles

| Documento | Descripción | Audiencia |
|-----------|-------------|-----------|
| `MIGRATION.md` | Documentación técnica detallada | Desarrolladores |
| `MIGRATION_SUMMARY.md` | Resumen ejecutivo de cambios | Project Managers, DevOps |
| `VALIDATION.md` | Guía de testing y validación | QA, Testers |
| `CHANGELOG.md` | Historial de cambios | Todos |

---

## 🚀 Instalación rápida

### Para nueva instalación:
```bash
odoo-bin -d <database> -i product_template_tags
```

### Para actualización desde V17:
```bash
odoo-bin -d <database> -u product_template_tags
```

---

## ✨ Características

- ✅ Tags en productos (product.template)
- ✅ Jerarquía de tags (parent/child)
- ✅ Colores personalizables
- ✅ Multi-compañía
- ✅ Contador de productos
- ✅ Vistas mejoradas (Kanban, Lista)
- ✅ Filtros y búsquedas
- ✅ Traducible

---

## 🔧 Cambios principales en V19

1. **API actualizada**: Método `_check_recursion()` simplificado
2. **Imports modernizados**: Tests usan nueva estructura
3. **Sintaxis XML corregida**: Opciones con formato correcto
4. **100% compatible** con datos de V17

Ver `CHANGELOG.md` para detalles completos.

---

## 📞 Soporte

- **Repositorio OCA:** https://github.com/OCA/product-attribute
- **Documentación Odoo:** https://www.odoo.com/documentation/19.0/
- **Issues:** https://github.com/OCA/product-attribute/issues

---

## 👥 Mantenedores

- @patrickrwilson
- @ivantodorovich

---

**Migrado el:** 4 de marzo de 2026  
**Por:** GitHub Copilot  
**Estado:** ✅ Listo para producción
