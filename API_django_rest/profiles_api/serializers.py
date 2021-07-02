from rest_framework import serializers

# seriaizador de JSON convierte objetos python en info JSOn similar a formulario de django, paa convertir en json info


class TransactionSerializer(serializers.Serializer):
    """ Serializa un campo para probar nuestro API """
    option = serializers.IntegerField()
    
    #apellido = serializers.CharField(max_length=20)
