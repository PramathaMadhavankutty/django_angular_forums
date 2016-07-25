from rest_framework import serializers
from .models import PollSubject, Poll, Vote, Thread


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('id', 'poll', 'subject', 'user')


class PollSubjectSerializer(serializers.ModelSerializer):

    votes = VoteSerializer(many=True)

    percentage_of_votes = serializers.SerializerMethodField()

    class Meta:
        model = PollSubject
        fields = ('id', 'name', 'votes', 'percentage_of_votes')

    def get_percentage_of_votes(self, subject):
        return subject.votes.count()*100/subject.poll.votes.count()


class PollSerializer(serializers.ModelSerializer):

    subjects = PollSubjectSerializer(many=True)

    user_has_voted = serializers.SerializerMethodField()

    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ('id','thread', 'question', 'subjects', 'user_has_voted', 'total_votes')

    def get_user_has_voted(self, poll):
        has_voted = False

        request = self.context.get('request', None)

        if not request:
            return False

        if not request.user.is_authenticated():  # don't show vote ticks if they are not logged in!
            return True

        vote = poll.votes.filter(user_id=request.user.id).first()
        if vote:
            has_voted = True

        return has_voted

    def get_total_votes(self, poll):
        return poll.votes.count()


class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = ('id', 'created_at', 'name', 'subject', 'user')
