import React, { useState } from 'react';
import { ThemedView } from '@/components/ThemedView';
import { TextInput, Button, StyleSheet } from 'react-native';
import { Link } from 'expo-router';
import { useAuth } from '@/context/AuthContext';
import { ThemedText } from '@/components/ThemedText';
import { Redirect } from 'expo-router';

const LogIn = () => {
  const { logIn, user } = useAuth();

  const [error, setError] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogIn = async () => {
    try {
      await logIn(email, password);
    } catch (error: any) {
      console.error(error);
      setError(error.message);
    }
  };

  if (user) {
    return <Redirect href='/' />;
  }

  return (
    <ThemedView style={styles.container}>
      <ThemedText style={styles.error}>{error}</ThemedText>
      <TextInput
        style={styles.input}
        placeholder='Email'
        autoCapitalize='none'
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        style={styles.input}
        placeholder='Password'
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <Link href='./forgot-password'>Forgot Password</Link>
      <Link href='./register'>Create an account</Link>
      <Button title='Log In' onPress={handleLogIn} />
    </ThemedView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  input: {
    width: '100%',
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 12,
    paddingHorizontal: 8,
  },
  error: {
    color: 'red',
    marginBottom: 12,
  },
});

export default LogIn;
