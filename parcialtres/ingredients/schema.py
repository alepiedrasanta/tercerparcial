import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from ingredients.models import Category
from graphql_relay.node.node import from_global_id
 
class ComputadoraNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['marca', 'detalles','precio']
        interfaces = (relay.Node, )
 
class CrearComputadora(graphene.relay.ClientIDMutation):
    computadora = graphene.Field(ComputadoraNode)
    class Input:
        marca = graphene.String()
        detalles = graphene.String()
        precio = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        computadora = Category(
            marca=input.get('marca'),
            detalles=input.get('detalles'),
            precio=input.get('precio'),
        )
        computadora.save()
        return CrearComputadora(computadora=computadora)
 
 
class ActualizarComputadora(graphene.relay.ClientIDMutation):
    computadora = graphene.Field(ComputadoraNode)
    class Input:
        id = graphene.String()
        marca = graphene.String()
        detalles = graphene.String()
        precio = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        computadora = Category.objects.get(pk=from_global_id(input.get('id'))[1])
        computadora.marca = input.get('marca')
        computadora.detalles = input.get('detalles')
        computadora.precio = input.get('precio')
        computadora.save()
        return ActualizarComputadora(computadora=computadora)
  
class Query(graphene.ObjectType):
    computadora = relay.Node.Field(ComputadoraNode)
    todascomputadoras = DjangoFilterConnectionField(ComputadoraNode)
 
class Mutation(graphene.AbstractType):
    crearcomputadora = CrearComputadora.Field()
    actualizarcomputadora = ActualizarComputadora.Field()
