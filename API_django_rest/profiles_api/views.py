#from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers # modulo serializars.py
from profiles_api.authorizations import *
from profiles_api.authorization_with_capture import *


#import requests # temp

class TransactionApiView(APIView):

    serializer_class = serializers.TransactionSerializer

    """ Clase API view de prueba """
    def get(self, request, format=None):
        """Retorna lista de caracteristicas del APIView"""
        an_apiview = [
            'API developed using Python SDK to interact with Cybersource',
            'Transaction info such as customers credit card and other details are hardcoded',
            'In the Option field enter one of the following options:',
            '1 to send a payment with auth and capture in separate steps',
            '2 to send a payment with auth and capture on a single step',
            '3 to void an auth transaction',
            '4 to process a payment and request a refund',
            '5 to trigger one decision manager rejection rule, rejecting transactions using a particular e-mail',

        ]
         #la informacion para mostrar en json debe ser lista o diccionario
        return Response({'message': 'Welcome', 'INSTRUCTIONS': an_apiview})
            

    def post(self, request):
        """realiza transaccion de acuerdo con una condicion"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            option = serializer.validated_data.get('option')
            if option == 1:
                salida = capture_payment()
                return Response(json.loads(salida))
                
            elif option == 2:
                salida = authorization_with_capturesale()
                return Response(json.loads(salida))

            elif option == 3:
                salida = process_authorization_reversal()
                return Response(json.loads(salida))

            elif option == 4:
                salida = refund_payment()
                return Response(json.loads(salida))

            elif option == 5:
                salida = authorization_with_capturesale_trig_rej()
                return Response(json.loads(salida))

            else:
                return Response({'message':'Opcion inválida!'})

            
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':"DELETE"})


