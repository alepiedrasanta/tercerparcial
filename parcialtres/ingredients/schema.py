import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from ingredients.models import Category
from graphql_relay.node.node import from_global_id
 
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['marca', 'detalles','precio']
        interfaces = (relay.Node, )
 
class CreateCategory(graphene.relay.ClientIDMutation):
    category = graphene.Field(CategoryNode)
    class Input:
        marca = graphene.String()
        detalles = graphene.String()
        precio = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        category = Category(
            marca=input.get('marca'),
            detalles=input.get('detalles'),
            precio=input.get('precio'),
        )
        category.save()
        return CreateCategory(category=category)
 
 
class UpdateCategory(graphene.relay.ClientIDMutation):
    category = graphene.Field(CategoryNode)
    class Input:
        id = graphene.String()
        marca = graphene.String()
        detalles = graphene.String()
        precio = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        category = Category.objects.get(pk=from_global_id(input.get('id'))[1])
        category.marca = input.get('marca')
        category.detalles = input.get('detalles')
        category.precio = input.get('precio')
        category.save()
        return UpdateCategory(category=category)
 
 
class DeleteCategory(graphene.relay.ClientIDMutation):
    category = graphene.Field(CategoryNode)
 
    class Input:
        id = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        category = Category.objects.get(pk=from_global_id(input.get('id'))[1])
        category.delete()
        return DeleteCategory(category=category)
 
class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
 
class Mutation(graphene.AbstractType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()