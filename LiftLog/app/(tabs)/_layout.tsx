import { Redirect, Tabs } from 'expo-router';
import React from 'react';

import { TabBarIcon } from '@/components/navigation/TabBarIcon';
import { Colors } from '@/constants/Colors';
import { useColorScheme } from '@/hooks/useColorScheme';
import { useAuth } from '@/context/AuthContext';

export default function TabLayout() {
  const { initializing, user } = useAuth();
  const colorScheme = useColorScheme();

  if (initializing) {
    return null;
  }

  if (!user) {
    return <Redirect href='../log-in' />;
  }

  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: Colors[colorScheme ?? 'light'].tint,
        headerShown: false,
      }}
    >
      <Tabs.Screen
        name='index'
        options={{
          title: 'Home',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon name={focused ? 'home' : 'home'} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name='log'
        options={{
          title: 'Log',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon
              name={focused ? 'edit-note' : 'edit-note'}
              color={color}
            />
          ),
        }}
      />
      <Tabs.Screen
        name='exercises'
        options={{
          title: 'Exercises',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon
              name={focused ? 'fitness-center' : 'fitness-center'}
              color={color}
            />
          ),
        }}
      />
      <Tabs.Screen
        name='profile'
        options={{
          title: 'Profile',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon
              name={focused ? 'person' : 'person-outline'}
              color={color}
            />
          ),
        }}
      />
    </Tabs>
  );
}
