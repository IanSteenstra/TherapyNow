from rest_framework import serializers

from .models import Profile, UserQuiz, CounselorQuiz
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

'''
Serializers convert model fields to Python data types in the form
of a dictionary. (i think)
'''
class ProfileSerializer(serializers.ModelSerializer):
  username = serializers.SerializerMethodField()

  def create(self, validated_data):
    user = User(
      email=validated_data['email'],
      username=validated_data['username']
    )
    user.set_password(validated_data['password'])
    user.save()
    profile = Profile(user=user)
    profile.save()
    return profile

  class Meta:
    model = Profile
    fields = ('username', 'user', 'alias')
    extra_kwargs = {'password': {'write_only': True}}


  def get_username(self, obj):
    return obj.user.username

class UserQuizSerializer(serializers.ModelSerializer):
  profile = serializers.SerializerMethodField()
  happiness = serializers.FloatField()
  hometown = serializers.FloatField()
  receiving_giving = serializers.FloatField()
  religion = serializers.FloatField()
  relation_to_others = serializers.FloatField()
  government_assistance = serializers.FloatField()
  local_community = serializers.FloatField()
  immediate_family = serializers.FloatField()
  fulfilling_work = serializers.FloatField()
  leader_social_circle = serializers.FloatField()
  created = serializers.DateTimeField()

  class Meta:
    nodel = UserQuiz
    fields = ('profile', 'happiness', 'hometown', 'receiving_giving', 'religion', 'relation_to_others', 'government_assistance'
              'local_community','immediate_family','fulfilling_work','leader_social_circle', 'created')

  def create(self, validated_data):
    profile = Profile(
      username=validated_data['username'],
      alias=validated_data['alias'],
    )
    profile.save()
    userQuiz = UserQuiz(
      profile=profile,
      happiness=validated_data['happiness'],
      hometown=validated_data['hometown'],
      receiving_giving=validated_data['receiving_giving'],
      religion=validated_data['religion'],
      relation_to_others=validated_data['relation_to_others'],
      government_assistance=validated_data['government_assistance'],
      local_community=validated_data['local_community'],
      immediate_family=validated_data['immediate_family'],
      fulfilling_work=validated_data['fulfilling_work'],
      leader_social_circle=validated_data['leader_social_circle'],
      created=validated_data['created'],
    )
    userQuiz.save()
    return userQuiz

  def update(self, instance, validated_data):
    instance.profile = validated_data.get('profile', instance.profile)
    instance.happiness = validated_data.get('happiness', instance.happiness)
    instance.hometown = validated_data.get('hometown', instance.hometown)
    instance.receiving_giving = validated_data.get('receiving_giving', instance.receiving_giving)
    instance.religion = validated_data.get('religion', instance.religion)
    instance.relation_to_others = validated_data.get('relation_to_others', instance.relation_to_others)
    instance.government_assistance = validated_data.get('government_assistance', instance.government_assistance)
    instance.local_community = validated_data.get('local_community', instance.local_community)
    instance.immediate_family = validated_data.get('immediate_family', instance.immediate_family)
    instance.fulfilling_work = validated_data.get('fulfilling_work', instance.fulfilling_work)
    instance.leader_social_circle = validated_data.get('leader_social_circle', instance.leader_social_circle)
    instance.created = validated_data.get('created', instance.created)
    return instance

class CounselorQuizSerializer(serializers.ModelSerializer): 
  profile = serializers.SerializerMethodField()
  a1 = serializers.FloatField()
  a2 = serializers.FloatField()
  a3 = serializers.FloatField()
  a4 = serializers.FloatField()
  a5 = serializers.FloatField()
  a6 = serializers.FloatField()
  a7 = serializers.FloatField()
  a8 = serializers.FloatField()
  a9 = serializers.FloatField()
  a10 = serializers.FloatField()
  created = serializers.DateTimeField()

  class Meta:
    nodel = CounselorQuiz
    fields = ('profile', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'
              'a7','a8','a9','a10', 'created')

  def create(self, validated_data):
    profile = Profile(
      username=validated_data['username'],
      alias=validated_data['alias'],
    )
    profile.save()
    counselorQuiz = CounselorQuiz(
      profile=profile,
      a1=validated_data['a1'],
      a2=validated_data['a2'],
      a3=validated_data['a3'],
      a4=validated_data['a4'],
      a5=validated_data['a5'],
      a6=validated_data['a6'],
      a7=validated_data['a7'],
      a8=validated_data['a8'],
      a9=validated_data['a9'],
      a10=validated_data['a10'],
      created=validated_data['created'],
    )
    counselorQuiz.save()
    return counselorQuiz

  def update(self, instance, validated_data):
    instance.profile = validated_data.get('profile', instance.profile)
    instance.a1 = validated_data.get('a1', instance.a1)
    instance.a2 = validated_data.get('a2', instance.a2)
    instance.a3 = validated_data.get('a3', instance.a3)
    instance.a4 = validated_data.get('a4', instance.a4)
    instance.a5 = validated_data.get('a5', instance.a5)
    instance.a6 = validated_data.get('a6', instance.a6)
    instance.a7 = validated_data.get('a7', instance.a7)
    instance.a8 = validated_data.get('a8', instance.a8)
    instance.a9 = validated_data.get('a9', instance.a9)
    instance.a10 = validated_data.get('a10', instance.a10)
    instance.created = validated_data.get('created', instance.created)
    return instance
