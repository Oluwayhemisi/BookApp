from rest_framework import serializers

from third_app.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):  # noqa
    # book_title = serializers.CharField(max_length=255, source='title')
    # publisher = PublisherSerializer()
#    publisher = serializers.HyperlinkedRelatedField(
#        queryset=Publisher.objects.all(),
 #       view_name='third_app:publisher-detail'

    #)

    class Meta:
        model = Book
        fields = "__all__"
        fields = ['title', 'description', 'date_published', 'isbn', 'price', 'publisher']
        # exclude =[]
