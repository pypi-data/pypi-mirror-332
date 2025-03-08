import argparse
import datetime
import time
from enum import Enum
from functools import lru_cache
from itertools import cycle
from zoneinfo import ZoneInfo

from blessed import Terminal

from market_clock.get_market_info import ALL_MARKET_INFO


class NextTradingEvent(Enum):
    SAME_DAY_FULL_DAY_CLOSE = 0
    SAME_DAY_HALF_DAY_CLOSE = 1
    SAME_DAY_OPEN = 2
    SAME_DAY_LUNCH_START = 3
    SAME_DAY_LUNCH_END = 4
    NEXT_TRADING_DAY_START = 5


@lru_cache
def get_next_trading_day(start_date, holidays, trading_weekdays):
    holidays = set(holidays)
    trading_weekdays = set(trading_weekdays)

    next_day = start_date + datetime.timedelta(days=1)
    while True:
        if next_day.weekday() in trading_weekdays and next_day not in holidays:
            return next_day
        next_day += datetime.timedelta(days=1)


def format_timedelta(delta):
    total_seconds = int(delta.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def get_market_status(market_name, market_info):
    timezone = market_info["timezone"]
    trading_weekdays = market_info["trading_weekdays"]
    holidays = market_info["holidays"]
    half_days = market_info["half_days"]
    start_time = market_info["start_time"]
    end_time = market_info["end_time"]
    half_day_end_time = market_info["half_day_end_time"]
    is_have_lunch_break = market_info["is_have_lunch_break"]
    if is_have_lunch_break:
        lunch_break_start = market_info["lunch_break_start"]
        lunch_break_end = market_info["lunch_break_end"]

    local_time = datetime.datetime.now(timezone)
    current_time = local_time.time()
    current_date = local_time.date()

    if current_date > max(holidays | half_days):
        msg = f"{market_name} holiday list is not up-to-date."
        raise ValueError(msg)
    if holidays & half_days:
        msg = f"{market_name} has overlapping holidays/half-days"
        raise ValueError(msg)

    if (local_time.weekday() not in trading_weekdays) or (current_date in holidays):
        is_open = False
        next_trading_event = NextTradingEvent.NEXT_TRADING_DAY_START
    # Assume in half day lunch break is cancelled
    elif current_date in half_days:
        is_open = start_time <= current_time <= half_day_end_time

        if is_open:
            next_trading_event = NextTradingEvent.SAME_DAY_HALF_DAY_CLOSE

        elif current_time < start_time:
            next_trading_event = NextTradingEvent.SAME_DAY_OPEN

        elif current_time > half_day_end_time:
            next_trading_event = NextTradingEvent.NEXT_TRADING_DAY_START

    # Normal trading day
    elif (
        current_date not in holidays
        and current_date not in half_days
        and local_time.weekday() in trading_weekdays
    ):
        if is_have_lunch_break:
            if current_time < start_time:
                is_open = False
                next_trading_event = NextTradingEvent.SAME_DAY_OPEN

            elif start_time <= current_time < lunch_break_start:
                is_open = True
                next_trading_event = NextTradingEvent.SAME_DAY_LUNCH_START

            elif lunch_break_start <= current_time < lunch_break_end:
                is_open = False
                next_trading_event = NextTradingEvent.SAME_DAY_LUNCH_END

            elif lunch_break_end <= current_time < end_time:
                is_open = True
                next_trading_event = NextTradingEvent.SAME_DAY_FULL_DAY_CLOSE

            elif current_time >= end_time:
                is_open = False
                next_trading_event = NextTradingEvent.NEXT_TRADING_DAY_START

            else:
                msg = "Unhandled case."
                raise ValueError(msg)
        else:
            if current_time < start_time:
                is_open = False
                next_trading_event = NextTradingEvent.SAME_DAY_OPEN

            elif start_time <= current_time < end_time:
                is_open = True
                next_trading_event = NextTradingEvent.SAME_DAY_FULL_DAY_CLOSE

            elif current_time >= end_time:
                is_open = False
                next_trading_event = NextTradingEvent.NEXT_TRADING_DAY_START

            else:
                msg = "Unhandled case."
                raise ValueError(msg)

    if next_trading_event == NextTradingEvent.SAME_DAY_OPEN:
        event_date, event_time = current_date, start_time

    elif next_trading_event == NextTradingEvent.SAME_DAY_HALF_DAY_CLOSE:
        event_date, event_time = current_date, half_day_end_time

    elif next_trading_event == NextTradingEvent.SAME_DAY_FULL_DAY_CLOSE:
        event_date, event_time = current_date, end_time

    elif next_trading_event == NextTradingEvent.SAME_DAY_LUNCH_START:
        event_date, event_time = current_date, lunch_break_start

    elif next_trading_event == NextTradingEvent.SAME_DAY_LUNCH_END:
        event_date, event_time = current_date, lunch_break_end

    elif next_trading_event == NextTradingEvent.NEXT_TRADING_DAY_START:
        event_date, event_time = (
            get_next_trading_day(
                current_date, tuple(holidays), tuple(trading_weekdays)
            ),
            start_time,
        )
    else:
        msg = "Unhandled case."
        raise ValueError(msg)

    next_event_date_time_utc = datetime.datetime.combine(
        event_date, event_time, tzinfo=timezone
    ).astimezone(ZoneInfo("UTC"))

    return is_open, next_event_date_time_utc


def main():
    parser = argparse.ArgumentParser(description="Market Clock Options")
    
    # Add argument to show seconds, default is to hide them
    parser.add_argument('--show-seconds', action='store_true', help='Show seconds in the output')
    
    # Add argument to specify markets, default is to show all
    parser.add_argument('--markets', nargs='+', help='List of markets to show', default=[])

    # Add argument to list supported markets
    parser.add_argument('--list-markets', action='store_true', help='List all supported markets')

    args = parser.parse_args()

    # Check if the --list-markets argument is provided
    if args.list_markets:
        print("Supported Markets:")
        for market in ALL_MARKET_INFO.keys():
            print(f"- {market}")
        return
    term = Terminal()
    spinner = cycle("🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦")

    # Filter markets based on the --markets argument
    markets_to_display = args.markets if args.markets else ALL_MARKET_INFO.keys()
    longest_market_name_length = max(len(k) for k in markets_to_display)

    with term.fullscreen(), term.hidden_cursor():
        while True:
            spinner_char = next(spinner)

            clock_lines = []

            for market in markets_to_display:
                is_open, event = get_market_status(market, ALL_MARKET_INFO[market])

                # Format timedelta based on --show-seconds argument
                time_delta = event - datetime.datetime.now(ZoneInfo('UTC'))
                formatted_time_delta = format_timedelta(time_delta) if args.show_seconds else format_timedelta(time_delta)[:-3]
                clock_line = (
                    f"{market.rjust(longest_market_name_length)} "
                    f"{'OPENED 🟢' if is_open else 'CLOSED 🟠'} | "
                    f"{'Closes' if is_open else 'Opens '} in "
                    f"{formatted_time_delta} "
                    f"{spinner_char}"
                )

                clock_lines.append(clock_line)

            clock_lines = "\n".join(clock_lines)

            clock = term.move(0, 0) + term.clear_eos + clock_lines

            # Update display
            print(clock)
            time.sleep(1)


if __name__ == "__main__":
    main()
