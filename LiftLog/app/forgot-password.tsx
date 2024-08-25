import React, { useState } from 'react';
import { ThemedView } from '@/components/ThemedView';
import { TextInput, Button, Alert, StyleSheet } from 'react-native';

const ForgotPasswordForm: React.FC = () => {
  const [email, setEmail] = useState('');

  const handleResetPassword = () => {
    // TODO: Implement password reset logic here
    Alert.alert(
      'Password Reset',
      `An email has been sent to ${email} with instructions to reset your password.`
    );
  };

  return (
    <ThemedView style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder='Email'
        value={email}
        onChangeText={setEmail}
        autoCapitalize='none'
        keyboardType='email-address'
      />
      <Button title='Reset Password' onPress={handleResetPassword} />
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
});

export default ForgotPasswordForm;
