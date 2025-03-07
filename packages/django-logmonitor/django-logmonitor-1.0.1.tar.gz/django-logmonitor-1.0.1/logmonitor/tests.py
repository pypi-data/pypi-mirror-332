from django.test import TestCase, RequestFactory
from django.test import TransactionTestCase

from django.contrib.auth.models import User
from logmonitor.models import LogMonitor, TestModel, UUIDModel
from logmonitor.signals import pre_save_handler, registrar_creacion_actualizacion, registrar_eliminacion
from django.db.models.signals import pre_save, post_save, post_delete
from django.contrib.sessions.models import Session
from datetime import datetime, timedelta
import time
from django.db import transaction

class LogMonitorTests(TransactionTestCase):  # Asegurar que es TransactionTestCase
    def setUp(self):
        """Configura un objeto de prueba para todas las pruebas."""
        self.test_object = TestModel.objects.create(
            name='Test Object', 
            description='This is a test object.'
        )

    def tearDown(self):
        # Desconectar señales después de cada prueba
        pre_save.disconnect(pre_save_handler, sender=TestModel)
        post_save.disconnect(registrar_creacion_actualizacion, sender=TestModel)
        post_delete.disconnect(registrar_eliminacion, sender=TestModel)

    def test_creacion_de_objeto(self):
        """Prueba que se registre la creación de un objeto."""
        # Crear un objeto de prueba (TestModel)
        test_object = TestModel.objects.create(name='Test Object', description='This is a test object.')

        # Verificar que se haya creado un registro en LogMonitor
        log_entry = LogMonitor.objects.filter(objeto_id=str(test_object.pk)).first()
        self.assertIsNotNone(log_entry)
        self.assertEqual(log_entry.accion, LogMonitor.ACTION_CREATE)
        self.assertEqual(log_entry.model_name, 'testmodel')  # Nombre del modelo en minúsculas
        self.assertEqual(log_entry.objeto_id, str(test_object.pk))

    def test_actualizacion_de_objeto(self):
        """Prueba que se registre la actualización de un objeto."""
        test_object = TestModel.objects.create(name='Test Object', description='This is a test object.')

        # Actualizar el objeto
        test_object.name = 'Updated Test Object'
        test_object.save()

        # Buscar el log correcto
        log_entry = LogMonitor.objects.filter(
            objeto_id=str(test_object.pk),  # Asegurar coincidencia exacta
            accion=LogMonitor.ACTION_UPDATE
        ).order_by('-fecha_hora').first()

        print(f"Log de actualización encontrado: {log_entry}")  # Depuración

        self.assertIsNotNone(log_entry)
        self.assertEqual(log_entry.accion, LogMonitor.ACTION_UPDATE)
        self.assertEqual(log_entry.model_name, 'testmodel')
        self.assertEqual(log_entry.objeto_id, str(test_object.pk))

    def test_manejo_de_diferentes_tipos_de_pk(self):
        """Prueba que se manejen correctamente diferentes tipos de claves primarias."""
        # Crear un objeto con una clave primaria UUID
        uuid_object = UUIDModel.objects.create(id='123e4567-e89b-12d3-a456-426614174000', name='UUID Object')

        # Verificar que se haya creado un registro en LogMonitor
        log_entry = LogMonitor.objects.filter(objeto_id=str(uuid_object.pk)).first()
        self.assertIsNotNone(log_entry)
        self.assertEqual(log_entry.objeto_id, str(uuid_object.pk))

    def test_exclusion_de_modelos(self):
        """Prueba que los modelos excluidos no se auditen."""
        # Crear una sesión con todos los campos obligatorios
        session = Session.objects.create(
            session_key='test_session_key',
            session_data='test_data',
            expire_date=datetime.now() + timedelta(days=1)  # Campo obligatorio
        )

        # Verificar que no se haya creado un registro en LogMonitor
        log_entry = LogMonitor.objects.filter(objeto_id=session.session_key).first()
        self.assertIsNone(log_entry)  # No debe haber registro para el modelo excluido

    def test_eliminacion_de_objeto(self):
        """Prueba que se registre la eliminación de un objeto ya existente."""
        objeto_id = str(self.test_object.pk)  # Guardar el ID antes de eliminar

        self.test_object.delete()

        # Esperar un poco para evitar problemas de concurrencia
        import time
        time.sleep(0.1)

        # Buscar el log correcto
        log_entry = LogMonitor.objects.filter(
            objeto_id=objeto_id,  # Usar el ID guardado en vez de self.test_object.pk
            accion=LogMonitor.ACTION_DELETE
        ).order_by('-fecha_hora').first()

        print(f"🔥 Log de eliminación encontrado: {log_entry}")  # Depuración

        self.assertIsNotNone(log_entry)
        self.assertEqual(log_entry.accion, LogMonitor.ACTION_DELETE)
        self.assertEqual(log_entry.objeto_id, objeto_id)



