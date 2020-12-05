class Utils {
    static shuffleArray = (array) => {
        const tmp = [ ...array ];
        for (let i = tmp.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [tmp[i], tmp[j]] = [tmp[j], tmp[i]];
        }
        return [ ...tmp ];
    }

    static generateRandomString = (len, chars) => {
        let result = '';
        const charset = chars ? chars : 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789{}[]"\'';
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

    static average = (values) => {
        const sum = values.reduce((a, b) => a + b, 0);
        return (sum / values.length) || 0;
    }
}

module.exports = Utils;