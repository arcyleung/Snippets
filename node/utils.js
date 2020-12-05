class Utils {
    static shuffleArray = (array) => {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }

    static generateRandomString = (len, chars) => {
        let result = '';
        const charset = chars ? chars : 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        for (let ix = 0; ix < len; ix++) {
            result += charset.charAt(Math.floor(Math.random() * charset.length));
        }
        return result;
    }

    static generateRandomStringArray = (len, chars, numStrings) => {
        let result = [];
        for (let ix = 0; ix < numStrings; ix++) {
            result.push(this.generateRandomString(len, chars));
        }
        return result;
    }
}

module.exports = Utils;