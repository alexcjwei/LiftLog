import { Stack } from 'expo-router/stack';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen
        name='index'
        options={{
          title: 'Profile',
          headerShown: false,
        }}
      />
      <Stack.Screen
        name='settings'
        options={{
          title: 'Settings',
        }}
      />
    </Stack>
  );
}
