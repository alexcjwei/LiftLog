import { ScrollView, StyleSheet } from 'react-native';
import { useAuth } from '@/context/AuthContext';
import SimpleView from '@/components/BaseView';
import { useState } from 'react';
import { ActivityCard } from '@/components/feed/ActivityCard';
import { ThemedText } from '@/components/ThemedText';

const dummyFeed = [
  {
    id: '1',
    user: {
      name: 'Alex Wei',
    },
    datetime: 'September 17, 2024 at 10:30 AM',
    location: 'Boston, MA',
    name: 'Lower Body',
  },
];
export default function HomeScreen() {
  const { user } = useAuth();
  const [feed, setFeed] = useState(dummyFeed);

  return (
    <SimpleView>
      <ThemedText type='title'>Welcome {user?.email}</ThemedText>
      <ScrollView>
        {feed.map((activity) => (
          <ActivityCard key={activity.id} {...activity} />
        ))}
      </ScrollView>
    </SimpleView>
  );
}

const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
});
