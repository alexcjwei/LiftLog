import { useState } from 'react';
import { ThemedView } from '@/components/ThemedView';
import { ThemedText } from '@/components/ThemedText';
import { useAuth } from '@/context/AuthContext';
import { StyleSheet, TextInput, Button } from 'react-native';
import { ThemedTextInput } from '@/components/ThemedTextInput';

export default function Register() {
  const { register } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');

  const handleRegister = async () => {
    const passwordError = validatePassword(password);
    if (passwordError) {
      setError(passwordError);
      return;
    } else if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    try {
      await register(email, password);
    } catch (error: any) {
      console.error(error);
      setError(error.message);
    }
  };

  return (
    <ThemedView>
      <ThemedText style={styles.error}>{error}</ThemedText>
      <ThemedTextInput
        style={styles.input}
        placeholder='Email'
        autoCapitalize='none'
        value={email}
        onChangeText={setEmail}
      />
      <ThemedTextInput
        style={styles.input}
        placeholder='Password'
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <ThemedTextInput
        style={styles.input}
        placeholder='Confirm Password'
        secureTextEntry
        value={confirmPassword}
        onChangeText={setConfirmPassword}
      />
      <Button title='Register' onPress={handleRegister} />
    </ThemedView>
  );
}

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
    marginBottom: 8,
  },
});

function validatePassword(password: string): string | null {
  const minLength = 8;
  const hasUppercase = /[A-Z]/.test(password);
  const hasLowercase = /[a-z]/.test(password);
  const hasNumber = /\d/.test(password);
  const hasSpecialChar = /[^A-Za-z0-9]/.test(password);

  if (password.length < minLength) {
    return 'Password must be at least 8 characters long.';
  }
  //   } else if (!hasUppercase) {
  //     return 'Password must contain at least one uppercase letter.';
  //   } else if (!hasLowercase) {
  //     return 'Password must contain at least one lowercase letter.';
  //   } else if (!hasNumber) {
  //     return 'Password must contain at least one number.';
  //   } else if (!hasSpecialChar) {
  //     return 'Password must contain at least one special character.';
  //   }

  return null;
}
