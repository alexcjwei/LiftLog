import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  PropsWithChildren,
} from 'react';
import {
  onAuthStateChanged,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  User,
} from 'firebase/auth';
import { auth } from '@/firebaseConfig';

interface AuthContextType {
  initializing: boolean;
  user: User | null;
  logIn: (email: string, password: string) => void;
  register: (email: string, password: string) => void;
  logOut: () => void;
}

export const AuthContext = createContext<AuthContextType>({
  initializing: true,
  user: null,
  logIn: () => null,
  register: () => null,
  logOut: () => null,
});

export const AuthProvider = ({ children }: PropsWithChildren) => {
  const [initializing, setInitializing] = useState(true);
  const [user, setUser] = useState<User | null>(null);

  const logIn = async (email: string, password: string) => {
    const userCredential = await signInWithEmailAndPassword(
      auth,
      email,
      password
    );
    console.log(userCredential);
    setUser(userCredential.user);
  };

  const register = async (email: string, password: string) => {
    console.log(email);
    const userCredential = await createUserWithEmailAndPassword(
      auth,
      email,
      password
    );
    console.log(userCredential);
    setUser(userCredential.user);
  };

  const handleOnAuthStateChanged = (user: User | null) => {
    setUser(user);
    if (initializing) {
      setInitializing(false);
    }
  };

  useEffect(() => {
    const subscriber = onAuthStateChanged(auth, handleOnAuthStateChanged);
    return subscriber; // unsubscribe on unmount
  }, []);

  return (
    <AuthContext.Provider
      value={{
        initializing,
        user,
        logIn: logIn,
        register: register,
        logOut: () => {
          setUser(null);
        },
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
