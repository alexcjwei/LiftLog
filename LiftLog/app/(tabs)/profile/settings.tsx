import SimpleView from '@/components/BaseView';
import { Button } from 'react-native';
import { ThemedText } from '@/components/ThemedText';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'expo-router';

export default function SettingsScreen() {
  const { logOut } = useAuth();
  const router = useRouter();

  const handleLogoutPress = () => {
    logOut();
    router.replace('/');
  };
  return (
    <SimpleView>
      <Button title='Logout' onPress={handleLogoutPress} />
    </SimpleView>
  );
}
