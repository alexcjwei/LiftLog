import { Stack } from 'expo-router/stack';

export default function Layout() {
  const getDetailTitle = (id: number) => `Workout ${id}`;

  return (
    <Stack>
      <Stack.Screen
        name='index'
        options={{
          title: 'Logs',
          headerShown: false,
        }}
      />
      <Stack.Screen
        name='[id]'
        options={({ route }) => ({
          title: getDetailTitle(route.params?.id) || 'Workout Log',
        })}
      />
    </Stack>
  );
}
