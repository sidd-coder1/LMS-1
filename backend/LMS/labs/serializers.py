from rest_framework import serializers
from .models import User, Lab, PC, Software, Equipment, MaintenanceLog, Inventory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'role')

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'

class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = ('id', 'lab', 'name', 'status', 'brand', 'serial_number')
        read_only_fields = ('id', 'lab')

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class MaintenanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceLog
        fields = '__all__'

class InventorySerializer(serializers.Serializer):
    """
    Dynamic Inventory Serializer - doesn't use the Inventory model directly.
    Instead, it serializes calculated inventory data from Equipment.
    """
    id = serializers.CharField(read_only=True)
    lab = serializers.IntegerField()
    equipment_type = serializers.CharField()
    total_quantity = serializers.IntegerField()
    working_quantity = serializers.IntegerField()
    not_working_quantity = serializers.IntegerField()
    under_repair_quantity = serializers.IntegerField()
