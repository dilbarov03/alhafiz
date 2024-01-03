from rest_framework import serializers

from .models import News, Gallery, Service, Hotel, Transport, TarifPricing, TarifService, Tarif, Application


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "body", "image", "created_at")
        
        
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ("id", "image", "youtube_link", "order")   
        

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("id", "name", "logo", "star", "distance", "image1", "image2", 
                  "image3", "image4", "image5")
        

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "name", "icon")     


class TarifServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarifService
        fields = ("id", "service")
        
    def to_representation(self, instance):
        return ServiceSerializer(instance.service, context=self.context).data


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ("id", "title", "subtitle", "body", "image1", "image2", "image3")


class TarifPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarifPricing
        fields = ("id", "title", "people_count", "price", "order")


class TarifListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = ("id", "title", "start_time", "end_time")


class TarifDetailSerializer(serializers.ModelSerializer):
    Makkah_hotel = HotelSerializer()
    Madinah_hotel = HotelSerializer()
    transport = TransportSerializer()
    services = TarifServiceSerializer(many=True)
    
    class Meta:
        model = Tarif
        fields = ("id", "title", "body", "start_time", "end_time", "days_in_Makkah", "days_in_Madinah",
                  "Makkah_hotel", "Madinah_hotel", "transport", "services")


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ("id", "tarif", "people_count", "name", "phone", "month")
