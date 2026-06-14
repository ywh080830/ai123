import { useState } from 'react';
import { Sidebar } from './components/Sidebar';
import { DashboardPage } from './pages/DashboardPage';
import { ActivationPage } from './pages/ActivationPage';
import { useAdminStore } from './stores/adminStore';

function App() {
  const [currentPage, setCurrentPage] = useState('dashboard');
  const { theme } = useAdminStore();

  // 应用主题
  useState(() => {
    if (theme === 'system') {
      const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      document.documentElement.classList.toggle('dark', isDark);
    } else {
      document.documentElement.classList.toggle('dark', theme === 'dark');
    }
  });

  const renderPage = () => {
    switch (currentPage) {
      case 'dashboard':
        return <DashboardPage />;
      case 'activation':
        return <ActivationPage />;
      case 'users':
        return (
          <div className="p-6">
            <h1 className="text-2xl font-bold text-gray-900 dark:text-white">用户管理</h1>
            <p className="text-gray-500 dark:text-gray-400 mt-2">功能开发中...</p>
          </div>
        );
      case 'orders':
        return (
          <div className="p-6">
            <h1 className="text-2xl font-bold text-gray-900 dark:text-white">订单管理</h1>
            <p className="text-gray-500 dark:text-gray-400 mt-2">功能开发中...</p>
          </div>
        );
      case 'models':
        return (
          <div className="p-6">
            <h1 className="text-2xl font-bold text-gray-900 dark:text-white">模型管理</h1>
            <p className="text-gray-500 dark:text-gray-400 mt-2">功能开发中...</p>
          </div>
        );
      case 'settings':
        return (
          <div className="p-6">
            <h1 className="text-2xl font-bold text-gray-900 dark:text-white">系统设置</h1>
            <p className="text-gray-500 dark:text-gray-400 mt-2">功能开发中...</p>
          </div>
        );
      default:
        return <DashboardPage />;
    }
  };

  return (
    <div className="flex min-h-screen bg-gray-50 dark:bg-gray-900">
      <Sidebar currentPage={currentPage} onNavigate={setCurrentPage} />
      <main className="flex-1 overflow-auto">
        {renderPage()}
      </main>
    </div>
  );
}

export default App;
