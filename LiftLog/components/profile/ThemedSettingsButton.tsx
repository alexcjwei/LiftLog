import { useThemeColor } from '@/hooks/useThemeColor';
import Ionicons from '@expo/vector-icons/Ionicons';
import { Link } from 'expo-router';
import { useColorScheme } from 'react-native';

export default function ThemedSettingsButton() {
  const theme = useColorScheme() ?? 'light';
  const color = useThemeColor({ light: 'black', dark: 'white' }, 'icon');

  return (
    <Link href='/profile/settings' style={{ marginRight: 10 }}>
      <Ionicons
        name={theme === 'light' ? 'settings' : 'settings-outline'}
        size={24}
        color={color}
      />
    </Link>
  );
}
