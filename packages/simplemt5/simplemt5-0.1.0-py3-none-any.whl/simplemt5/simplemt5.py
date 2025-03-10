import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

class SimpleMT5:
    """
    Упрощенная библиотека для работы с MetaTrader 5
    """
    
    def __init__(self):
        """
        Инициализация подключения к MetaTrader 5
        
        Args:
            path (str, optional): Путь к терминалу MetaTrader 5
            login (int, optional): Логин для подключения к счету
            password (str, optional): Пароль для подключения к счету
            server (str, optional): Сервер для подключения
        """
        # Инициализация подключения к MetaTrader 5
        if not mt5.initialize():
            print(f"Ошибка инициализации MetaTrader 5: {mt5.last_error()}")
            mt5.shutdown()
            raise Exception("Ошибка инициализации MetaTrader 5")
                
        # Словарь для преобразования строковых таймфреймов в константы MT5
        self.timeframes = {
            "M1": mt5.TIMEFRAME_M1,
            "M5": mt5.TIMEFRAME_M5,
            "M15": mt5.TIMEFRAME_M15,
            "M30": mt5.TIMEFRAME_M30,
            "H1": mt5.TIMEFRAME_H1,
            "H4": mt5.TIMEFRAME_H4,
            "D1": mt5.TIMEFRAME_D1,
            "W1": mt5.TIMEFRAME_W1,
            "MN1": mt5.TIMEFRAME_MN1
        }
    
    def __del__(self):
        """
        Закрытие подключения при удалении объекта
        """
        mt5.shutdown()
    
    def get_data(self, symbol, timeframe, count):
        """
        Получение исторических данных по символу
        
        Args:
            symbol (str): Символ (валютная пара)
            timeframe (str): Таймфрейм (M1, M5, M15, M30, H1, H4, D1, W1, MN1)
            count (int): Количество свечей
            
        Returns:
            pandas.DataFrame: Данные в формате pandas DataFrame с колонками [time, open, high, low, close]
        """
        # Проверка наличия символа
        if not mt5.symbol_info(symbol):
            print(f"Символ {symbol} не найден")
            return None
        
        # Проверка таймфрейма
        if timeframe not in self.timeframes:
            print(f"Неверный таймфрейм: {timeframe}. Доступные таймфреймы: {list(self.timeframes.keys())}")
            return None
        
        # Получение данных
        rates = mt5.copy_rates_from_pos(symbol, self.timeframes[timeframe], 0, count)
        
        if rates is None or len(rates) == 0:
            print(f"Не удалось получить данные для {symbol} на таймфрейме {timeframe}")
            return None
        
        # Преобразование в pandas DataFrame
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        
        # Удаление ненужных столбцов
        if 'tick_volume' in df.columns:
            df = df.drop('tick_volume', axis=1)
        if 'spread' in df.columns:
            df = df.drop('spread', axis=1)
        if 'real_volume' in df.columns:
            df = df.drop('real_volume', axis=1)
        
        # Оставляем только нужные столбцы в определенном порядке
        df = df[['time', 'open', 'high', 'low', 'close']]
        
        return df
    
    def buy(self, symbol, volume, take_profit=None, stop_loss=None, tp_points=None, sl_points=None, comment="Buy order"):
        """
        Открытие позиции на покупку
        
        Args:
            symbol (str): Символ (валютная пара)
            volume (float): Объем позиции в лотах
            take_profit (float, optional): Уровень тейк-профита (абсолютное значение цены)
            stop_loss (float, optional): Уровень стоп-лосса (абсолютное значение цены)
            tp_points (int, optional): Уровень тейк-профита в пунктах от текущей цены
            sl_points (int, optional): Уровень стоп-лосса в пунктах от текущей цены
            comment (str, optional): Комментарий к ордеру
            
        Returns:
            dict: Результат выполнения запроса
        """
        return self._open_position(symbol, volume, mt5.ORDER_TYPE_BUY, take_profit, stop_loss, tp_points, sl_points, comment)
    
    def sell(self, symbol, volume, take_profit=None, stop_loss=None, tp_points=None, sl_points=None, comment="Sell order"):
        """
        Открытие позиции на продажу
        
        Args:
            symbol (str): Символ (валютная пара)
            volume (float): Объем позиции в лотах
            take_profit (float, optional): Уровень тейк-профита (абсолютное значение цены)
            stop_loss (float, optional): Уровень стоп-лосса (абсолютное значение цены)
            tp_points (int, optional): Уровень тейк-профита в пунктах от текущей цены
            sl_points (int, optional): Уровень стоп-лосса в пунктах от текущей цены
            comment (str, optional): Комментарий к ордеру
            
        Returns:
            dict: Результат выполнения запроса
        """
        return self._open_position(symbol, volume, mt5.ORDER_TYPE_SELL, take_profit, stop_loss, tp_points, sl_points, comment)
    
    def _open_position(self, symbol, volume, order_type, take_profit=None, stop_loss=None, tp_points=None, sl_points=None, comment=""):
        """
        Внутренний метод для открытия позиции
        
        Args:
            symbol (str): Символ (валютная пара)
            volume (float): Объем позиции в лотах
            order_type (int): Тип ордера (BUY/SELL)
            take_profit (float, optional): Уровень тейк-профита (абсолютное значение цены)
            stop_loss (float, optional): Уровень стоп-лосса (абсолютное значение цены)
            tp_points (int, optional): Уровень тейк-профита в пунктах от текущей цены
            sl_points (int, optional): Уровень стоп-лосса в пунктах от текущей цены
            comment (str, optional): Комментарий к ордеру
            
        Returns:
            dict: Результат выполнения запроса
        """
        # Проверка наличия символа
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info is None:
            print(f"Символ {symbol} не найден")
            return None
        
        # Проверка доступности символа для торговли
        if not symbol_info.visible:
            print(f"Символ {symbol} не доступен, пробуем включить")
            if not mt5.symbol_select(symbol, True):
                print(f"Не удалось включить символ {symbol}")
                return None
        
        # Получение текущей цены
        price = mt5.symbol_info_tick(symbol).ask if order_type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(symbol).bid
        
        # Получение размера пункта (point) для символа
        point = symbol_info.point
        
        # Расчет уровней TP и SL на основе пунктов, если они заданы
        if tp_points is not None and tp_points > 0:
            if order_type == mt5.ORDER_TYPE_BUY:
                take_profit = price + (tp_points * point)
            else:  # SELL
                take_profit = price - (tp_points * point)
        
        if sl_points is not None and sl_points > 0:
            if order_type == mt5.ORDER_TYPE_BUY:
                stop_loss = price - (sl_points * point)
            else:  # SELL
                stop_loss = price + (sl_points * point)
        
        # Расчет уровней TP и SL, если они заданы в виде цены
        if take_profit is not None and take_profit > 0:
            if order_type == mt5.ORDER_TYPE_BUY:
                if take_profit <= price:
                    print("Уровень Take Profit должен быть выше текущей цены для ордера BUY")
                    return None
            else:  # SELL
                if take_profit >= price:
                    print("Уровень Take Profit должен быть ниже текущей цены для ордера SELL")
                    return None
        
        if stop_loss is not None and stop_loss > 0:
            if order_type == mt5.ORDER_TYPE_BUY:
                if stop_loss >= price:
                    print("Уровень Stop Loss должен быть ниже текущей цены для ордера BUY")
                    return None
            else:  # SELL
                if stop_loss <= price:
                    print("Уровень Stop Loss должен быть выше текущей цены для ордера SELL")
                    return None
        
        # Подготовка запроса
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": order_type,
            "price": price,
            "deviation": 10,  # Допустимое отклонение от запрошенной цены
            "magic": 12345,   # Идентификатор эксперта
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,  # Срок действия ордера - до отмены
            "type_filling": mt5.ORDER_FILLING_FOK,  # Тип заполнения ордера
        }
        
        # Добавление TP и SL, если они заданы
        if take_profit is not None and take_profit > 0:
            request["tp"] = take_profit
        
        if stop_loss is not None and stop_loss > 0:
            request["sl"] = stop_loss
        
        # Отправка запроса
        result = mt5.order_send(request)
        
        # Обработка результата
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"Ошибка открытия позиции: {result.retcode}")
            print(f"Описание: {result.comment}")
            return None
        
        print(f"Позиция успешно открыта: {result.order}")
        return {
            "order": result.order,
            "volume": volume,
            "price": price,
            "type": "BUY" if order_type == mt5.ORDER_TYPE_BUY else "SELL",
            "take_profit": take_profit,
            "stop_loss": stop_loss
        }
    
    def get_account_info(self):
        """
        Получение информации о счете
        
        Returns:
            dict: Информация о счете
        """
        account_info = mt5.account_info()
        if account_info is None:
            print("Не удалось получить информацию о счете")
            return None
        
        return {
            "balance": account_info.balance,
            "equity": account_info.equity,
            "profit": account_info.profit,
            "margin": account_info.margin,
            "margin_level": account_info.margin_level,
            "margin_free": account_info.margin_free
        }
    
    def get_positions(self, symbol=None):
        """
        Получение открытых позиций
        
        Args:
            symbol (str, optional): Символ (валютная пара)
            
        Returns:
            list: Список открытых позиций
        """
        positions = mt5.positions_get(symbol=symbol) if symbol else mt5.positions_get()
        
        if positions is None or len(positions) == 0:
            return []
        
        result = []
        for position in positions:
            pos = {
                "ticket": position.ticket,
                "symbol": position.symbol,
                "type": "BUY" if position.type == mt5.ORDER_TYPE_BUY else "SELL",
                "volume": position.volume,
                "price_open": position.price_open,
                "price_current": position.price_current,
                "profit": position.profit,
                "take_profit": position.tp,
                "stop_loss": position.sl,
                "time": datetime.fromtimestamp(position.time)
            }
            # Добавляем специальный метод для строкового представления
            pos["__str__"] = lambda p=pos: f"Тикет: {p['ticket']}, {p['symbol']}, {p['type']}, Объем: {p['volume']}, Прибыль: {p['profit']}"
            result.append(PositionInfo(pos))
        
        return result
    
    def get_positions_simple(self, symbol=None):
        """
        Максимально упрощенное получение открытых позиций
        
        Args:
            symbol (str, optional): Символ (валютная пара)
            
        Returns:
            list: Список открытых позиций в упрощенном формате
        """
        positions = mt5.positions_get(symbol=symbol) if symbol else mt5.positions_get()
        
        if positions is None or len(positions) == 0:
            return []
        
        result = []
        for position in positions:
            result.append(SimplePosition(
                position.ticket,
                position.symbol,
                "BUY" if position.type == mt5.ORDER_TYPE_BUY else "SELL",
                position.volume,
                position.profit,
                position.tp,
                position.sl
            ))
        
        return result
    
    def buy_simple(self, symbol, volume, tp_points=100, sl_points=50):
        """
        Упрощенное открытие позиции на покупку с указанием TP и SL в пунктах
        
        Args:
            symbol (str): Символ (валютная пара)
            volume (float): Объем позиции в лотах
            tp_points (int): Уровень тейк-профита в пунктах от текущей цены (по умолчанию 100)
            sl_points (int): Уровень стоп-лосса в пунктах от текущей цены (по умолчанию 50)
            
        Returns:
            dict: Результат выполнения запроса
        """
        return self._open_position(symbol, volume, mt5.ORDER_TYPE_BUY, None, None, tp_points, sl_points, "Simple Buy")
    
    def sell_simple(self, symbol, volume, tp_points=100, sl_points=50):
        """
        Упрощенное открытие позиции на продажу с указанием TP и SL в пунктах
        
        Args:
            symbol (str): Символ (валютная пара)
            volume (float): Объем позиции в лотах
            tp_points (int): Уровень тейк-профита в пунктах от текущей цены (по умолчанию 100)
            sl_points (int): Уровень стоп-лосса в пунктах от текущей цены (по умолчанию 50)
            
        Returns:
            dict: Результат выполнения запроса
        """
        return self._open_position(symbol, volume, mt5.ORDER_TYPE_SELL, None, None, tp_points, sl_points, "Simple Sell")
    
    def close_positions(self, symbol=None):
        """
        Закрытие всех открытых позиций по указанному символу
        Если символ не указан, закрываются все позиции
        
        Args:
            symbol (str, optional): Символ (валютная пара)
            
        Returns:
            bool: True, если все позиции успешно закрыты, иначе False
        """
        # Получение открытых позиций
        positions = mt5.positions_get(symbol=symbol) if symbol else mt5.positions_get()
        
        if positions is None or len(positions) == 0:
            print(f"Нет открытых позиций{' по ' + symbol if symbol else ''}")
            return True
        
        # Закрытие каждой позиции
        success = True
        for position in positions:
            # Определение типа ордера для закрытия (противоположный текущему)
            order_type = mt5.ORDER_TYPE_SELL if position.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
            
            # Подготовка запроса на закрытие
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": position.symbol,
                "volume": position.volume,
                "type": order_type,
                "position": position.ticket,
                "price": mt5.symbol_info_tick(position.symbol).ask if order_type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(position.symbol).bid,
                "deviation": 10,
                "magic": 12345,
                "comment": f"Close position #{position.ticket}",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_FOK,
            }
            
            # Отправка запроса
            result = mt5.order_send(request)
            
            # Обработка результата
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                print(f"Ошибка закрытия позиции #{position.ticket}: {result.retcode}")
                print(f"Описание: {result.comment}")
                success = False
            else:
                print(f"Позиция #{position.ticket} успешно закрыта")
        
        return success
    
    def modify_tp_sl(self, ticket, tp=None, sl=None, tp_points=None, sl_points=None):
        """
        Изменение тейк-профита и стоп-лосса для существующей позиции
        
        Args:
            ticket (int): Тикет позиции
            tp (float, optional): Новый уровень тейк-профита (абсолютное значение)
            sl (float, optional): Новый уровень стоп-лосса (абсолютное значение)
            tp_points (int, optional): Новый уровень тейк-профита в пунктах от текущей цены
            sl_points (int, optional): Новый уровень стоп-лосса в пунктах от текущей цены
            
        Returns:
            bool: True, если изменение успешно, иначе False
        """
        # Получение позиции по тикету
        position = mt5.positions_get(ticket=ticket)
        if position is None or len(position) == 0:
            print(f"Позиция с тикетом {ticket} не найдена")
            return False
        
        position = position[0]
        
        # Получение информации о символе
        symbol_info = mt5.symbol_info(position.symbol)
        if symbol_info is None:
            print(f"Символ {position.symbol} не найден")
            return False
        
        # Получение текущей цены
        current_price = mt5.symbol_info_tick(position.symbol).ask if position.type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(position.symbol).bid
        
        # Получение размера пункта для символа
        point = symbol_info.point
        
        # Расчет уровней TP и SL на основе пунктов, если они заданы
        if tp_points is not None and tp_points > 0:
            if position.type == mt5.ORDER_TYPE_BUY:
                tp = current_price + (tp_points * point)
            else:  # SELL
                tp = current_price - (tp_points * point)
        
        if sl_points is not None and sl_points > 0:
            if position.type == mt5.ORDER_TYPE_BUY:
                sl = current_price - (sl_points * point)
            else:  # SELL
                sl = current_price + (sl_points * point)
        
        # Если TP и SL не заданы, используем текущие значения
        if tp is None:
            tp = position.tp
        
        if sl is None:
            sl = position.sl
        
        # Подготовка запроса на изменение
        request = {
            "action": mt5.TRADE_ACTION_SLTP,
            "symbol": position.symbol,
            "position": position.ticket,
            "tp": tp,
            "sl": sl
        }
        
        # Отправка запроса
        result = mt5.order_send(request)
        
        # Обработка результата
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"Ошибка изменения TP/SL для позиции #{position.ticket}: {result.retcode}")
            print(f"Описание: {result.comment}")
            return False
        
        print(f"TP/SL для позиции #{position.ticket} успешно изменены")
        return True
    
    def modify_tp_sl_simple(self, ticket, tp_points=None, sl_points=None):
        """
        Упрощенное изменение тейк-профита и стоп-лосса в пунктах
        
        Args:
            ticket (int): Тикет позиции
            tp_points (int, optional): Новый уровень тейк-профита в пунктах от текущей цены
            sl_points (int, optional): Новый уровень стоп-лосса в пунктах от текущей цены
            
        Returns:
            bool: True, если изменение успешно, иначе False
        """
        return self.modify_tp_sl(ticket, tp_points=tp_points, sl_points=sl_points)

class PositionInfo(dict):
    """
    Класс для удобного представления информации о позиции
    """
    def __str__(self):
        return f"Тикет: {self['ticket']}, {self['symbol']}, {self['type']}, Объем: {self['volume']}, Прибыль: {self['profit']}"

class SimplePosition:
    """
    Класс для максимально простого представления позиции
    """
    def __init__(self, ticket, symbol, type, volume, profit, tp, sl):
        self.ticket = ticket
        self.symbol = symbol
        self.type = type
        self.volume = volume
        self.profit = profit
        self.tp = tp
        self.sl = sl
    
    def __str__(self):
        return f"Тикет: {self.ticket}, {self.symbol}, {self.type}, Объем: {self.volume}, Прибыль: {self.profit}"
    
    def __repr__(self):
        return self.__str__() 