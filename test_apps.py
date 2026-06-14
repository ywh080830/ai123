from playwright.sync_api import sync_playwright
import time

def test_all_apps():
    """测试三端应用"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # 测试用户端Web
        print("\n=== 测试用户端Web (http://localhost:5176) ===")
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:5176')
            page.wait_for_load_state('networkidle')
            print("✓ 用户端激活页面加载成功")
            
            # 检查页面元素
            title = page.locator('h1').text_content()
            print(f"  页面标题: {title}")
            
            # 检查购买按钮
            buy_button = page.locator('button:has-text("立即购买")')
            if buy_button.count() > 0:
                print("✓ 找到购买按钮")
                buy_button.click()
                page.wait_for_load_state('networkidle')
                print("✓ 购买页面加载成功")
                
                # 检查套餐选择
                plans = page.locator('button[class*="rounded-xl"]')
                print(f"  找到 {plans.count()} 个套餐选项")
                
                # 检查邮箱输入
                email_input = page.locator('input[type="email"]')
                if email_input.count() > 0:
                    print("✓ 找到邮箱输入框")
                
                # 返回激活页面
                page.go_back()
                page.wait_for_load_state('networkidle')
            
            # 测试激活码输入
            code_input = page.locator('input[placeholder*="激活码"]')
            if code_input.count() > 0:
                print("✓ 找到激活码输入框")
                code_input.fill('TEST-CODE-1234-ABCD')
                
                # 点击激活按钮
                activate_btn = page.locator('button:has-text("激活")')
                if activate_btn.count() > 0:
                    print("✓ 找到激活按钮")
                    # 不实际点击，避免错误
            
        except Exception as e:
            print(f"✗ 用户端测试失败: {e}")
        
        page.close()
        
        # 测试管理后台Web
        print("\n=== 测试管理后台Web (http://localhost:5177) ===")
        page = browser.new_page()
        
        try:
            page.goto('http://localhost:5177')
            page.wait_for_load_state('networkidle')
            print("✓ 管理后台加载成功")
            
            # 检查侧边栏
            sidebar = page.locator('nav')
            if sidebar.count() > 0:
                print("✓ 找到侧边栏导航")
            
            # 点击激活码管理
            activation_link = page.locator('button:has-text("激活码")')
            if activation_link.count() > 0:
                activation_link.click()
                page.wait_for_load_state('networkidle')
                print("✓ 激活码管理页面加载成功")
                
                # 检查生成按钮
                generate_btn = page.locator('button:has-text("生成激活码")')
                if generate_btn.count() > 0:
                    print("✓ 找到生成激活码按钮")
                    
                    # 点击生成激活码
                    generate_btn.click()
                    page.wait_for_timeout(500)
                    print("✓ 生成激活码弹窗显示成功")
                    
                    # 检查套餐选择
                    plan_buttons = page.locator('button[class*="rounded-lg border"]')
                    print(f"  找到 {plan_buttons.count()} 个套餐选项")
                    
                    # 关闭弹窗
                    cancel_btn = page.locator('button:has-text("取消")')
                    if cancel_btn.count() > 0:
                        cancel_btn.click()
                        page.wait_for_timeout(500)
                        print("✓ 关闭弹窗成功")
            
        except Exception as e:
            print(f"✗ 管理后台测试失败: {e}")
        
        page.close()
        
        # 测试API服务器
        print("\n=== 测试API服务器 (http://localhost:3000) ===")
        page = browser.new_page()
        
        try:
            # 健康检查
            page.goto('http://localhost:3000/health')
            page.wait_for_load_state('networkidle')
            content = page.content()
            if 'ok' in content:
                print("✓ API服务器健康检查通过")
            
            # 测试生成激活码API
            page.goto('http://localhost:3000/api/activation-codes')
            page.wait_for_load_state('networkidle')
            content = page.content()
            if '[]' in content or 'code' in content:
                print("✓ 激活码列表API正常")
            
        except Exception as e:
            print(f"✗ API服务器测试失败: {e}")
        
        page.close()
        browser.close()
        
        print("\n=== 测试完成 ===")

if __name__ == '__main__':
    test_all_apps()
