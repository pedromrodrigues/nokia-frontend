export function ISOtoString(dateString: string | null): string {
    if (dateString) {
        const date = new Date(dateString);
        const year = date.getFullYear();
        const month = date.getMonth();
        const day = date.getDate();
        const hour = date.getHours();
        const minutes = date.getMinutes();

        const monthString = month < 10 ? '0' + month : '' + month;
        const dayString = day < 10 ? '0' + day : '' + day;
        const hourString = hour < 10 ? '0' + hour : '' + hour;
        const minString = minutes < 10 ? '0' + minutes : '' + minutes;

        return `${year}-${monthString}-${dayString} ${hourString}:${minString}`
    } else {
        return '-';
    }
}