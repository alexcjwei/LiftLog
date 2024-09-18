import { ThemedView } from '@/components/ThemedView';
import { ThemedText } from '@/components/ThemedText';
import { StyleSheet } from 'react-native';
export interface CardProps {
  id: string;
  user: {
    name: string;
  };
  datetime: string;
  location: string;
  name: string;
}

export function ActivityCard(props: CardProps) {
  return (
    <ThemedView style={styles.card}>
      <ThemedView style={styles.content}>
        <ThemedText type='defaultSemiBold'>{props.user.name}</ThemedText>
        <ThemedView style={styles.subtitle}>
          <ThemedText>
            {props.datetime} - {props.location}
          </ThemedText>
        </ThemedView>
        <ThemedText type='subtitle'>{props.name}</ThemedText>
      </ThemedView>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  card: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 16,
    borderRadius: 8,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  subtitle: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  avatar: {
    width: 50,
    height: 50,
    borderRadius: 25,
    marginRight: 16,
  },
  content: {
    flex: 1,
  },
});
