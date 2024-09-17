import { Button, type ButtonProps } from 'react-native';
import { useThemeColor } from '@/hooks/useThemeColor';
export function ThemedButton({
  lightColor,
  darkColor,
  ...otherProps
}: ButtonProps & { lightColor?: string; darkColor?: string }) {
  const backgroundColor = useThemeColor(
    { light: lightColor, dark: darkColor },
    'background'
  );

  return <Button color={backgroundColor} {...otherProps} />;
}
