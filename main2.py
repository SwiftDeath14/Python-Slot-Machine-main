import random

MAX_LINES = 3  # Jumlah maksimal garis taruhan
MAX_BET = 500  # Taruhan maksimum per garis
MIN_BET = 1  # Taruhan minimum per garis

ROWS = 3  # Jumlah baris slot
COLS = 3  # Jumlah kolom slot

# Jumlah simbol yang muncul dalam mesin slot
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Nilai setiap simbol dalam mesin slot
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# Fungsi untuk memeriksa kemenangan berdasarkan garis taruhan
def check_winnings(columns, lines, bet, values):
    winnings = 0  # Total kemenangan
    winning_lines = []  # Daftar garis yang menang
    for line in range(lines):  # Iterasi untuk setiap garis taruhan
        symbol = columns[0][line]  # Simbol pada kolom pertama di garis tertentu
        for column in columns:  # Periksa setiap kolom di garis tersebut
            symbol_to_check = column[line]
            if symbol != symbol_to_check:  # Jika simbol berbeda, berhenti
                break
        else:  # Jika semua simbol cocok, tambahkan kemenangan
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# Fungsi untuk menghasilkan hasil putaran mesin slot
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # Daftar semua simbol berdasarkan jumlahnya
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []  # Daftar hasil untuk setiap kolom
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)  # Pilih simbol secara acak
            current_symbols.remove(value)  # Hapus simbol yang sudah dipilih
            column.append(value)

        columns.append(column)

    return columns


# Fungsi untuk mencetak hasil mesin slot
def print_slot_machine(columns):
    for row in range(len(columns[0])):  # Iterasi untuk setiap baris
        for i, column in enumerate(columns):  # Iterasi untuk setiap kolom
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Cetak simbol dengan pemisah
            else:
                print(column[row], end="")  # Cetak simbol terakhir tanpa pemisah
        print()  # Pindah ke baris berikutnya


# Fungsi untuk meminta pemain melakukan deposit
def deposit():
    while True:
        amount = input("Berapa jumlah deposit Anda? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:  # Deposit harus lebih besar dari 0
                break
            else:
                print("Jumlah harus lebih besar dari 0.")
        else:
            print("Masukkan angka.")

    return amount


# Fungsi untuk meminta jumlah garis taruhan
def get_number_of_lines():
    while True:
        lines = input(
            "Masukkan jumlah garis yang ingin Anda pertaruhkan (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # Validasi jumlah garis
                break
            else:
                print("Masukkan jumlah garis yang valid.")
        else:
            print("Masukkan angka.")

    return lines


# Fungsi untuk meminta jumlah taruhan per garis
def get_bet():
    while True:
        amount = input("Berapa taruhan Anda untuk setiap garis? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:  # Validasi batas taruhan
                break
            else:
                print(f"Jumlah harus antara ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Masukkan angka.")

    return amount


# Fungsi utama untuk menjalankan putaran mesin slot
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:  # Pastikan saldo mencukupi
            print(
                f"Saldo Anda tidak cukup untuk taruhan ini, saldo saat ini: ${balance}")
        else:
            break

    print(
        f"Anda bertaruh ${bet} pada {lines} garis. Total taruhan: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    # Tambahkan pesan jika pemain kalah
    if winnings == 0:
        print("Anda kalah.")
    else:
        print(f"Anda menang ${winnings}.")
        print(f"Anda menang pada garis:", *winning_lines)

    return winnings - total_bet



# Fungsi utama permainan
def main():
    balance = deposit()  # Memulai dengan deposit pemain
    while True:
        print(f"Saldo saat ini adalah ${balance}")
        answer = input("Tekan Enter untuk bermain (q untuk keluar).")
        if answer == "q":
            break
        balance += spin(balance)  # Perbarui saldo berdasarkan hasil putaran

    print(f"Anda keluar dengan saldo ${balance}")


main()
