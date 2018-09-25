from rest_framework.generics import (
			DestroyAPIView,
			UpdateAPIView,
			ListAPIView,
			RetrieveAPIView,
			CreateAPIView,
			)


from posts.models import Post

from .serializers import(
	PostDetailSerializer, 
	PostListSerializer,
	PostCreateUpdateSerializer,
	) 

'''The folowing views conteain all CRUD functionality through the API
All class views are named according to their functionality
'''

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer

##associate a user on create
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'


class PostUpdateAPIView(UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

