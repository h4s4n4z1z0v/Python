import socket  # şəbəkə bağlantıları üçün socket modulu
from concurrent.futures import ThreadPoolExecutor  # paralel işləmə üçün ThreadPoolExecutor

# Verilən IP-də bir portu yoxlamaq üçün funksiya
def scan_port(ip, port):
    try:
        # TCP socket yaradılır
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # bağlantı cəhdinin vaxt limiti (1 saniyə)
        result = sock.connect_ex((ip, port))  # bağlantı cəhdi edilir
        sock.close()  # socket bağlanır
        # Əgər connect_ex 0 qaytarırsa, port açıqdır
        return port if result == 0 else None
    except:
        # Hər hansı xəta (məsələn, səhv IP) olduqda None qaytarılır
        return None

# Verilən IP-də port aralığını yoxlamaq üçün funksiya
def port_scanner(ip, start_port=1, end_port=1024):
    open_ports = []  # açıq portları saxlayacaq siyahı
    # Paralel işləmək üçün 100 thread-lik ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Bütün portlar üçün scan_port işlərini submit edirik
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        # Nəticələr gəldikcə yoxlayırıq
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)  # açıq port siyahıya əlavə olunur
    return open_ports  # açıq portlar qaytarılır

if __name__ == "__main__":
    # İstifadəçidən IP ünvanı alınır
    target_ip = input("Hədəf IP ünvanını daxil edin: ").strip()
    print(f"{target_ip} ünvanında 1-dən 1024-ə qədər portlar yoxlanılır...")
    # Port scanner-i işə salırıq və açıq portları alırıq
    open_ports = port_scanner(target_ip)
    # Açıq portları çap edirik
    print(f"Açıq portlar: {open_ports}")
